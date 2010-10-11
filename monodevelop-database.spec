Name:     	monodevelop-database
Version:	2.4
Release:	%mkrel 2
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
BuildRequires:	mono-devel
BuildRequires:  monodevelop >= %version
BuildRequires:  gtksourceview-sharp-devel
%if %mdvver >= 200900
#gw this is not yet in 2008.1
BuildRequires:  mysql-connector-net
%endif
Summary:	Monodevelop Database Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Monodevelop Database Addin
	  

%prep
%setup -q
%if %mdvver >= 200900
cp -f %_prefix/lib/mono/mysql-connector-net/MySql.Data.dll contrib/MySql
%endif

%build
./configure --prefix=%_prefix
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_prefix/share/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%_prefix/share/pkgconfig
for langdir in %buildroot%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/locale/*; do
echo "%lang($(basename $langdir)) $(echo $langdir |sed s!%buildroot!!)" >> %name.lang
done
#gw don't provide this:
%if %mdvver >= 200900
ln -sf %_prefix/lib/mono/mysql-connector-net/MySql.Data.dll %buildroot%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/MySql.Data.dll
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %name.lang
%defattr(-, root, root)
%_prefix/share/pkgconfig/monodevelop-database.pc
%dir %_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.dll
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.mdb
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/icons/
%dir %_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/locale/

