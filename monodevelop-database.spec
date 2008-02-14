Name:     	monodevelop-database
Version:	0.18
Release:	%mkrel 1
License:	LGPL
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
BuildRequires:	mono-devel monodevelop >= 0.18
Summary:	Monodevelop Database Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Monodevelop Database Addin
	  

%prep
%setup -q

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


%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %name.lang
%defattr(-, root, root)
%_prefix/share/pkgconfig/monodevelop-database.pc
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.dll
%dir %_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/locale/

